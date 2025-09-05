from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, clips_array

TITLE_TEXT = "AI Agent Learning — CartPole (PPO)"
LEFT_LABEL = "Random Policy"
RIGHT_LABEL = "Trained PPO"
TRIM_SECONDS = 10  # keep the video punchy for LinkedIn
TITLE_SECONDS = 2


def main():
    # Load clips
    left = VideoFileClip("cartpole_random.mp4").subclip(0, TRIM_SECONDS)
    right = VideoFileClip("cartpole_policy.mp4").subclip(0, TRIM_SECONDS)

    # Match heights for clean hstack
    right = right.resize(height=left.h)

    # Labels on each half
    # (TextClip needs ImageMagick installed on macOS: `brew install imagemagick`)
    random_label = TextClip(LEFT_LABEL, fontsize=48, color="white", method="caption",
                            size=(left.w, 80)).set_position(("center", "top")).set_duration(left.duration)
    random_bg = TextClip("", size=(left.w, 90), color="black").set_position(
        ("center", "top")).set_duration(left.duration).set_opacity(0.5)

    trained_label = TextClip(RIGHT_LABEL, fontsize=48, color="white", method="caption",
                             size=(right.w, 80)).set_position(("center", "top")).set_duration(right.duration)
    trained_bg = TextClip("", size=(right.w, 90), color="black").set_position(
        ("center", "top")).set_duration(right.duration).set_opacity(0.5)

    left_labeled = CompositeVideoClip([left,  random_bg,  random_label])
    right_labeled = CompositeVideoClip([right, trained_bg, trained_label])

    # Side-by-side
    side_by_side = clips_array([[left_labeled, right_labeled]])

    # Title card (full width of both videos)
    title = TextClip(TITLE_TEXT, fontsize=56, color="white", method="caption",
                     size=(side_by_side.w, 160)).set_duration(TITLE_SECONDS)
    title_bg = TextClip("", size=(side_by_side.w, 200),
                        color="black").set_duration(TITLE_SECONDS)
    title_card = CompositeVideoClip([title_bg, title])

    # Concatenate title + main
    final = CompositeVideoClip([side_by_side.set_start(TITLE_SECONDS)])
    final = CompositeVideoClip([title_card, final]).set_duration(
        TITLE_SECONDS + side_by_side.duration)

    # Export
    final.write_videofile("cartpole_before_after_pro.mp4",
                          fps=30, codec="libx264", audio=False)
    print("🎬 Saved cartpole_before_after_pro.mp4")


if __name__ == "__main__":
    main()
