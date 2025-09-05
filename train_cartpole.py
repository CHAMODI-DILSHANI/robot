import gymnasium as gym
from stable_baselines3 import PPO


def main():
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=50_000)
    model.save("ppo_cartpole")
    env.close()
    print("✅ Trained & saved to ppo_cartpole.zip")


if __name__ == "__main__":
    main()
