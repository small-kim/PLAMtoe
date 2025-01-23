from omni.isaac.lab.envs import DirectRLEnvCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sim import SimulationCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils import configclass

@configclass
class MyEnvCfg(DirectRLEnvCfg):
   # simulation
   sim: SimulationCfg = SimulationCfg()
   # robot
   robot_cfg: ArticulationCfg = ArticulationCfg()
   # scene
   scene: InteractiveSceneCfg = InteractiveSceneCfg()
   # env
   decimation = 2
   episode_length_s = 5.0
   action_space = 1
   observation_space = 4
   state_space = 0
   # task-specific parameters
   ...