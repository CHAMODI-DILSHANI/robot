import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
from stable_baselines3 import PPO


def evaluate(env_id, model=None, episodes=20):
    """Run episodes and return total rewards"""
    env = gym.make(env_id)
    rewards = []
    for _ in range(episodes):
        obs, _ = env.reset()
        terminated = truncated = False
        total_reward = 0
        while not (terminated or truncated):
            if model:
                action, _ = model.predict(obs, deterministic=True)
            else:
                action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    env.close()
    return rewards


def main():
    env_id = "CartPole-v1"

    # Load trained model
    model = PPO.load("ppo_cartpole")

    # Evaluate random vs trained
    random_rewards = evaluate(env_id, model=None)
    trained_rewards = evaluate(env_id, model=model)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.bar(["Random (avg)", "Trained (avg)"],
            [np.mean(random_rewards), np.mean(trained_rewards)],
            color=["red", "green"])
    plt.ylabel("Average Reward per Episode")
    plt.title("CartPole: Random vs Trained PPO Agent")

    # Save
    plt.savefig("reward_comparison.png", dpi=150)
    plt.show()
    print("📊 Saved reward_comparison.png")


if __name__ == "__main__":
    main()
