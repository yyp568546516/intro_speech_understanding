import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    
    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples
    
    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames
    
    num_frames should be at least int((len(speech)-frame_length)/step); it may be longer.
    For every n and t such that 0 <= t*step+n <= N-1, it should be the case that 
       frames[n,t] = waveform[t*step+n]
    '''
    num_frames = int((len(waveform) - frame_length) / step) + 1
    frames = np.zeros((frame_length, num_frames))
    for frame in range(num_frames):
        start = frame * step
        end = start + frame_length
        frames[:, frame] = waveform[start:end]     
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    
    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)
    
    @returns:
    stft (np.ndarray((frame_length,num_frames))) - the STFT (complex-valued)
    '''
 
    stft = np.fft.fft(frames, axis=0)  
    return stft

def stft_to_spectrogram(stft):
    '''
    Calculate the level, in decibels, of each complex-valued sample of the STFT,
    normalized so the highest value is 0dB, 
    and clipped so that the lowest value is -60dB.
    
    @params:
    stft (np.ndarray((frame_length,num_frames))) - STFT (complex-valued)
    
    @returns:
    spectrogram (np.ndarray((frame_length,num_frames)) - spectrogram (real-valued)
    
    The spectrogram should be expressed in decibels (20*log10(abs(stft)).
    np.amax(spectrogram) should be 0dB.
    np.amin(spectrogram) should be no smaller than -60dB.
    '''
    magnitude = np.abs(stft) ** 2 + 1e-10 
    spectrogram = 10 * np.log10(magnitude) 
    spectrogram -= np.amax(spectrogram)
    spectrogram = np.maximum(spectrogram, -60)
    return spectrogram

