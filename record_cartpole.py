import gymnasium as gym
import imageio
from stable_baselines3 import PPO


def main():
    # Load environment and trained model
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    model = PPO.load("ppo_cartpole")

    frames = []
    obs, _ = env.reset()
    terminated = truncated = False

    # Run the policy and collect frames
    while not (terminated or truncated):
        frames.append(env.render())
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)

    env.close()

    # Save to MP4 video
    imageio.mimsave("cartpole_policy.mp4", frames, fps=30)
    print("🎥 Saved video to cartpole_policy.mp4")


if __name__ == "__main__":
    main()
