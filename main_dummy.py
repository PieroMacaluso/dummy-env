from stable_baselines3 import DQN, PPO
from stable_baselines3.common.env_checker import check_env
from dummy_env import dummy
from pettingzoo.test import parallel_api_test


if __name__ == '__main__':
    # Testing the parallel algorithm alone
    env_parallel = dummy.parallel_env()
    parallel_api_test(env_parallel)  # This works!

    # Testing the environment with the wrapper
    env = dummy.petting_zoo()

    # ERROR: AssertionError: The observation returned by the `reset()` method does not match the given observation space 
    check_env(env)  

    # Model initialization
    model = PPO("MlpPolicy", env, verbose=1)
    
    # ERROR: AssertionError: The observation returned by the `reset()` method does not match the given observation space 
    model.learn(total_timesteps=10_000)
