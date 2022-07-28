from tabnanny import verbose
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.env_checker import check_env
from dummy_env import dummy
from pettingzoo.test import parallel_api_test
import supersuit as ss


if __name__ == '__main__':
    # Testing the parallel algorithm alone
    env_parallel = dummy.parallel_env()
    parallel_api_test(env_parallel)  # This works!

    # Testing the environment with the wrapper
    env = dummy.petting_zoo()

    # ERROR: AssertionError: Your environment must inherit from the gym.Env class cf https://github.com/openai/gym/blob/master/gym/core.py
    check_env(env_parallel)  

    # Model initialization
    model = PPO("MlpPolicy", env_parallel, verbose=1)
    
    # WORKS!
    model.learn(total_timesteps=10_000)
