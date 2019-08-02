import wave
import struct
import array
import itertools as it

def load(fname, args):
    # When the with block completes, the Wave_read.close() -docs.python.org/3/library/wave
    with wave.open(fname, 'rb') as file:
        params = file.getparams()
        nchannels, sampwidth, framerate, nframes, comptype, compname = params

        bytes = file.readframes(nframes) # Read all frames from audio
        fmt = "<"+str(nchannels*nframes)+"h"
        y = list(struct.unpack_from(fmt,bytes))

        if nchannels>1:
            result = []
            for i in range(nchannels):
                result.append(y[i::nchannels])
            return result, framerate
        else:
            return y, framerate


def save(data, fname, args):
    with wave.open(fname, 'wb') as file:
        y, framerate = data
        if type(y[0])==list:
            nchannels = len(y)
            nframes = len(y[0])
        else:
            nchannels = 1
            nframes = len(y)
        sampwidth = 2
        comptype = "NONE"
        compname = 'not compressed'
        params = nchannels, sampwidth, framerate, nframes, comptype, compname
        file.setparams(params)
        if nchannels == 1:
            bytes = array.array('h', y).tobytes()
            file.writeframes(bytes)
        else:
            stream = list(it.chain(*list(zip(*y)))) # Weaves all channels into one list
            bytes = array.array('h', stream).tobytes()
            file.writeframes(bytes)

def help():
    print("WAV")
    print("\tload(fname): Returns y, framerate")
    print("\t\ty: Audio data. If fname is a mono track file, y is a list of ints. Otherwise, y is a list of lists, where each list cooresponds to a separate track, e.g. for a stereo file y = [l,r] for left and right output")
    print("\t\tframerate: sample rate in Hz")
    print("\tsave(data,fname): data must be a tuple or list in the same format which is returned from load(fname), i.e. data = [y,framerate]")
    print("\tUsage:")
    print("\t\ty,sr = load('example.wav')")
    print("\t\ty = y[0] #Extract the left output from a stereo track")
    print("\t\tsave((y,sr),'mono.wav')")
