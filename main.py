from recog_gender import grab_screenshot, recog_gender
from render_gender import visualize, visualize_init, visualize_done
from threading import Timer
import numpy as np

WAIT_SECONDS = 1
def update_display():
    
    im = np.array(grab_screenshot())
    count_man, count_woman = recog_gender(image=im)
    print("update_display: ", "count_man:", count_man, "count_woman:", count_woman)
    visualize(count_man, count_woman)
    Timer(WAIT_SECONDS, update_display).start()

if __name__ == '__main__':
    visualize_init()
    update_display()
    visualize_done()