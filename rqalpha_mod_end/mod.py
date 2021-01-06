# -*- coding: utf-8 -*-
import os
import pickle
import subprocess

from rqalpha.interface import AbstractMod
from rqalpha.core.events import EVENT
from rqalpha.const import EXIT_CODE
#from rqalpha.utils.logger import std_log

class EndMod(AbstractMod):
    def __init__(self):
        self._env = None
        self.fields = None
        self.path = None
        self.name = None
        self.hooks = None

    def start_up(self, env, mod_config):
        self._env = env
        self.fields = mod_config.fields
        self.path = mod_config.path
        self.hooks = mod_config.hooks
        env.event_bus.add_listener(EVENT.POST_USER_INIT, self._init)

    def _init(self, event):
        self.path = self._env.config.base.output_dir
        self.name = self._env.config.base.output_file_prefix

    def tear_down(self, code, exception=None):
        if code != EXIT_CODE.EXIT_SUCCESS: return
        ucontext = self._env.user_strategy._user_context
        # write to files
        fields = set(self.fields)
        # auto-detect keys
        fields.update(['data', 'rebalance', 'calendar'])
        for field in fields:
            if field not in ucontext.__dict__: continue
            with open(os.path.join(self.path, self.name+'-'+field+'.pkl'), 'wb') as f:
                pickle.dump(ucontext.__dict__[field], f)
        # run post hooks
        hooks = set(self.hooks)
        hooks.update(['rq_pkl_analyser.py'])
        for cmd in hooks:
            cmds = cmd if isinstance(cmd, list) else [ cmd, ]
            if cmds[0].endswith('.py'):
                cmds.insert(0, 'python')
            #std_log.info('running hook: {}'.format(' '.join(cmds)))
            subprocess.run(cmds, capture_output=True)
