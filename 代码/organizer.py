from pathlib import Path
import shutil

target = Path(".")

folders = {
     "图片":[".jpg",".jpeg",".png",".gif"],
     "文档":[".doc",".docx",".pdf",".txt"],
     "视频":[".mp4",".avi",".mkv"],
     "音频":[".mp3",".wav",".flac"],
     "代码":[".py",".js",".html",".css"]
}

for f in target.iterdir():
    if f.is_file():
        moved = False
        for name,exts in folders.items():
            if f.suffix.lower() in exts:
                dest = target / name
                dest.mkdir(exist_ok=True)
                shutil.move(str(f),str(dest/f.name))
                print(f"已移动{f.name}到{dest}")
                moved = True
                break
        if not moved:
            print(f"未分类的文件:{f.name}")

