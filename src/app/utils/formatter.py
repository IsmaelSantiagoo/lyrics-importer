def format_for_projection(text: str, linhas_por_slide: int = 4) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    slides = []
    for i in range(0, len(lines), linhas_por_slide):
        slide = "\n".join(lines[i:i + linhas_por_slide])
        slides.append(slide)

    return "\n\n".join(slides)
