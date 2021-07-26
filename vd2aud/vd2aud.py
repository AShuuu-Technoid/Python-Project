import os
import moviepy.editor as mp
import subprocess

def vd2aud():
    gtpth=os.path.dirname(os.path.realpath(__file__))
    # Insert Local Video File Path

    infile=subprocess.check_output('read -e -p "Enter Full Path File: " var ; echo $var',shell=True).rstrip().decode('utf8')
    clip = mp.VideoFileClip(infile)

    base=os.path.basename(infile)
    fname=os.path.splitext(base)[0]
    # Insert Local Audio File Path
    outfn=(f"output/{fname}.mp3")
    fn = os.path.join(gtpth,outfn)
    clip.audio.write_audiofile(fn)

if __name__ == "__main__":
    vd2aud()
