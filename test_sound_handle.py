from sound_handle import SoundHandle


if __name__ == "__main__":
    sh = SoundHandle()

    sh.activate()
    sh.connect()

    with sh.client:


    sh.terminate()
