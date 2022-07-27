from gym.envs.registration import register

register(
    id='DummyEnv-v0',
    entry_point='dummy_env.dummy:parallel_env',
)