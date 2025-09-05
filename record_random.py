import gymnasium as gym
import imageio


def main():
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    frames = []
    obs, _ = env.reset()
    terminated = truncated = False
    while not (terminated or truncated):
        frames.append(env.render())
        action = env.action_space.sample()  # random = fails early
        obs, reward, terminated, truncated, info = env.step(action)
    env.close()
    imageio.mimsave("cartpole_random.mp4", frames, fps=30)
    print("🎥 Saved: cartpole_random.mp4")


if __name__ == "__main__":
    main()
