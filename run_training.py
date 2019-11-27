import glob
from time import sleep

import model_main_2 as train
import tensorflow as tf
from absl import flags
import os
import time


def main():
    TrainingsStepsBeforeCheck = 4000
    print("initialse autotraining...")
    subdirectory = "trainingdata"
    folders_in_subdirectory_old = []
    while 1:
        folders_in_subdirectory_new = getFoldersInSubdirecory(subdirectory)
        missing_folders = makeNewList(folders_in_subdirectory_new, folders_in_subdirectory_old)
        folders_in_subdirectory_old = getFoldersInSubdirecory(subdirectory)

        flags.FLAGS([""])

        for folder in missing_folders:
            try:
                configpath = glob.glob(os.path.join(folder, "*.config"))[0]
                flags.FLAGS.pipeline_config_path = configpath
                flags.FLAGS.model_dir = "training"
                flags.FLAGS.num_train_steps = TrainingsStepsBeforeCheck
                print(folder)
                print(flags.FLAGS.model_dir)

                initialTime = int(time.time)
                while True:
                    runTrainJob()
                    elapsedTime = time.time - initialTime
                    if(elapsedTime > 6*60*60)
                        break
                        
            except OSError as e:
                print(e)
            except IOError:
                print("Error occurred with %s. Try next config.." % folder)

        sleep(2)


def getFoldersInSubdirecory(path):
    folders_in_subdirectory = [os.path.join(path, o)
                               for o in os.listdir(path)
                               if os.path.isdir(os.path.join(path, o))]
    return folders_in_subdirectory


# @asyncio.coroutine
def runTrainJob():
    tf.app.run(train.main)


def makeNewList(list_new, list_old):
    new_list = [i for i in list_new if i not in list_old]

    return new_list


if __name__ == '__main__':
    main()
