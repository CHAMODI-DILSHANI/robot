# 🤖 Robot RL Demo – CartPole with PPO  

This project shows how to train a reinforcement learning (RL) agent to **balance a pole on a cart** — no hardware, just simulation.  

It’s a beginner-friendly but powerful demonstration of how robots learn:  
- **Random policy** → fails fast  
- **Trained PPO policy** → balances stably  

---

## 🎥 Demo  

| Random Policy | Trained PPO |  
|---------------|-------------|  
| ![Random](random.gif) | ![Trained](trained.gif) |  

👉 See full side-by-side video in the repo (`cartpole_comparison.mp4`).  

---

## ⚙️ How it Works  

- 🕹️ **Environment**: [Gymnasium – CartPole-v1](https://gymnasium.farama.org/)  
- 🧠 **Algorithm**: PPO from [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)  
- 🎯 **Reward signal**: *stay upright, don’t fall*  
- 📼 **Output**: Frames rendered → MP4 (via `imageio` / `moviepy`)  

---

## 📊 Results  

The trained PPO agent consistently outperforms a random policy:  

![Reward Comparison](reward_comparison.png)  

---

## 📂 Repository Structure  

├── train_cartpole.py # Train PPO agent

├── record_random.py # Record random policy

├── record_cartpole.py # Record trained policy

├── stitch_side_by_side.py # Combine random vs trained videos

├── plot_rewards.py # Plot performance comparison

├── ppo_cartpole.zip # Saved PPO model

├── *.mp4 # Generated demo videos

└── reward_comparison.png # Performance graph


---

## 🚀 Getting Started  

### 1. Install dependencies  

```bash
pip install -r requirements.txt
```
Or manually:

```bash
pip install stable-baselines3 gymnasium imageio moviepy matplotlib
```
2. Train an agent
```bash
python train_cartpole.py
```
3. Record random vs trained policies
```bash
python record_random.py
python record_cartpole.py
```
4. Create side-by-side comparison video
```bash
python stitch_side_by_side.py
```

💡 Next Steps
- Extend to MuJoCo Ant for 3D locomotion
- Add evaluation metrics + plots
- Explore more advanced reward shaping

📌 Author

👩‍💻 Built by Chamodi Dilshani
