from typing import Optional
from gym import spaces
import random
import numpy as np
from pettingzoo import ParallelEnv
from pettingzoo.utils.conversions import parallel_wrapper_fn
import supersuit as ss
from gym.utils import EzPickle, seeding


def env(**kwargs):
    env_ = parallel_env(**kwargs)
    env_ = ss.pettingzoo_env_to_vec_env_v1(env_)
    env_ = ss.concat_vec_envs_v1(env_, 1, base_class="stable_baselines3")
    return env_


petting_zoo = env


class parallel_env(ParallelEnv, EzPickle):
    metadata = {'render_modes': ['ansi'], "name": "PlayerEnv-Multi-v0"}

    def __init__(self, n_agents: int = 20, new_step_api: bool = True) -> None:
        EzPickle.__init__(
            self,
            n_agents,
            new_step_api
        )

        self._episode_ended = False
        self.n_agents = n_agents

        self.possible_agents = [
            f"player_{idx}" for idx in range(n_agents)]

        self.agents = self.possible_agents[:]

        self.agent_name_mapping = dict(
            zip(self.possible_agents, list(range(len(self.possible_agents))))
        )

        self.observation_spaces = spaces.Dict(
            {agent: spaces.Box(shape=(len(self.agents),),
                               dtype=np.float64, low=0.0, high=1.0) for agent in self.possible_agents}
        )

        self.action_spaces = spaces.Dict(
            {agent: spaces.Discrete(4) for agent in self.possible_agents}
        )
        self.current_step = 0

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]

    def __calculate_observation(self, agent_id: int) -> np.ndarray:
        return self.observation_space(agent_id).sample()

    def __calculate_observations(self) -> np.ndarray:
        observations = {
            agent: self.__calculate_observation(
                agent_id=agent)
            for agent in self.agents
        }
        return observations

    def observe(self, agent):
        return self.__calculate_observation(agent_id=agent)

    def step(self, actions):
        if self._episode_ended:
            return self.reset()
        observations = self.__calculate_observations()
        rewards = random.sample(range(100), self.n_agents)
        self.current_step += 1
        self._episode_ended = self.current_step >= 100
        infos = {agent: {} for agent in self.agents}
        dones = {agent: self._episode_ended for agent in self.agents}
        rewards = {
            self.agents[i]: rewards[i]
            for i in range(len(self.agents))
        }
        if self._episode_ended:
            self.agents = {}  # To satisfy `set(par_env.agents) == live_agents`
        return observations, rewards, dones, infos

    def reset(self,
              seed: Optional[int] = None,
              return_info: bool = False,
              options: Optional[dict] = None,):
        self.agents = self.possible_agents[:]
        self._episode_ended = False
        self.current_step = 0
        observations = self.__calculate_observations()
        return observations

    def render(self, mode="human"):
        # TODO: IMPLEMENT
        print("TO BE IMPLEMENTED")

    def close(self):
        pass
