from moviepy.editor import VideoFileClip, clips_array


def main():
    left = VideoFileClip("cartpole_random.mp4")
    right = VideoFileClip("cartpole_policy.mp4").resize(height=left.h)
    final = clips_array([[left, right]])
    final.write_videofile("cartpole_before_after.mp4", fps=30)
    print("🎬 Saved: cartpole_before_after.mp4")


if __name__ == "__main__":
    main()
