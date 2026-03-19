import re

with open('experience.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<svg viewBox="0 0 320 266".*?</svg>'
replacement = '<video src="assets/images/experience-page/business-team-generating-idea-animation-gif-download-5293511.mp4" width="90%" autoplay loop muted playsinline></video>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('experience.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement done!")
