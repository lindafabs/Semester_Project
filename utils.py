import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def plot_wave(x, y, xlim, ylim, label, col):
    '''
    plots signal
    # x : x axis points
    # y : value of the funtion evaluated in x
    # xlim : limit x axis
    # ylim : limit y axis
    # label: label for legend
    # col : color of line

    :return: plots
    '''
    plt.plot(x, y, color=col, linewidth=1, label = label)
    plt.xlim([0, xlim])
    plt.ylim([-ylim, ylim])
    plt.xlabel('time [s]', fontsize=10)
    plt.ylabel('Amplitude', fontsize=10)
    plt.grid()

def fourier_analysis(x, fsmp):
    '''
    Performs Fourier analysis of signal x
    # x : input signal
    # fsmp : reference to create frequency range vector

    :return: frequency range, FFT
    '''
    # Normalized Fast Fourier transform of simple sine wave
    X=np.fft.fft(x)
    X/=np.abs(X).max()
    # Frequency vector
    N = len(X)
    n = np.arange(N)
    T = N / fsmp
    #print('T: {}'.format(T))
    freq = n / T
    #print('freq: {}'.format(freq))
    #freqx = np.fft.fftfreq(len(x), x[1]-x[0])
    return freq, X


def fourier_plot(freq, X, freq_lim, title):
    '''
    Plots Fourier analysis
    # freq: frequency resolution
    # X: Fourier transform
    # freq_lim: limit on the x axis
    # title: title of the plot

    :return: plot
    '''
    plt.plot(freq, np.abs(X), 'b')
    #plt.stem(freq, np.abs(X), markerfmt='', linefmt='b' )
    plt.xlabel('Freq [Hz]')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, freq_lim)
    plt.ylim(0, 1)
    plt.grid()
    plt.title(title, fontsize=9)


def fourier_plot_db(freq, X, freq_lim, ylim, title):
    '''
    Plots Fourier analysis on dB scale
    # freq : frequency resolution
    # X : signal FFT
    # freq_lim : limit on the x axis plot
    # title : title of the plot

    :return: plot in dB scale
    '''
    plt.plot(freq, 20*np.log10(np.abs(X)))
    plt.xlabel('Freq [Hz]')
    plt.ylabel('FFT Amplitude [dB]')
    plt.xlim(0, freq_lim)
    plt.ylim(ylim, 10)
    plt.grid()
    plt.title(title, fontsize = 9)


def bitmap_plotter(qbits, matrix, time):
    '''
    Plots the position bits waves
    # qbits : number of quantization bits
    # matrix : matrix where each row is a position bit
    # time : time vector x axis
    :return: plot
    '''
    for i in range(qbits):
        plt.plot(time, matrix[i, :] + 2 * i, label='Bit idx: {}'.format(i))
    y_tick_labels = ['0', '1', '0', '1', '0', '1']
    plt.yticks([0, 1, 2, 3, 4, 5], y_tick_labels)
    plt.legend();
    plt.xlabel('Time [s]')
    plt.ylim(0, 6)
    plt.title('Binary encoding of the quantized signal', fontsize = 9)

def plot_quantized_all(t_ct, t_smp, y_ct, y_ct_q, y_smp_q, xlimit, ylimit):
    '''
    Plots original, quantized, sampled+quantized signals on the same curve

    # t_ct : time range for non-sampled signal
    # t_smp : time range for sampled signal
    # y_ct : y values of original signal
    # y_ct_q : y values of quantized signal
    # y_smp_q : y values of quantized and sampled signal
    # xlimit : limit on the x axis plot
    # ylimit : limit on the y axis plot

    :return: one plot with three curves
    '''

    fig = plt.figure(figsize = (10,4))
    plot_wave(t_ct, y_ct, xlimit, ylim=ylimit,label='Original signal', col='b')
    plot_wave(t_ct, y_ct_q, xlimit, ylim=ylimit,label='Quantized signal',col='g' )
    plot_wave(t_smp, y_smp_q, xlimit, ylim=ylimit,label='Quantized + sampled signal',col='r' )
    plt.title('Continuous time signal quantization',fontsize = 9)
    plt.legend();

def plot_fourier_three(freq_ct, X_ct, freq_q, X_q,  f_lim, freq_smp_q, X_smp_q):
    '''
    3 subplots showing the Fourier analysis of original signal, quantized signal, quantized + sampled signal
    # freq_ct : frequency resolution for continuous time signal
    # X_ct : Continuous time signal FFT
    # freq_q : frequency resolution for quantized signal
    # X_q : Quantized signal FFT
    # f_lim : limit on the x axis plot
    # freq_smp_q : frequency resolution for quantized + sampled signal
    # X_smp_q : Quantized + sampled signal FFT

    :return: subplot 1x3
    '''
    # linear
    plt.figure(figsize=(12, 5))
    plt.subplot(1,3,1)
    fourier_plot(freq_ct, X_ct, freq_lim=f_lim, title="Original continuous signal")
    plt.subplot(1,3,2)
    fourier_plot(freq_q, X_q, freq_lim=f_lim, title="Quantized signal")
    plt.subplot(1,3,3)
    fourier_plot(freq_smp_q, X_smp_q, freq_lim=f_lim, title="Quantized + sampled signal")
    plt.show()

    # dB
    plt.figure(figsize=(12, 5))
    plt.subplot(1,3,1)
    fourier_plot_db(freq_ct, X_ct, freq_lim=f_lim, ylim=-120, title="Original continuous signal")
    plt.subplot(1,3,2)
    fourier_plot_db(freq_q, X_q, freq_lim=f_lim, ylim= -120, title="Quantized signal")
    plt.subplot(1,3,3)
    fourier_plot_db(freq_smp_q, X_smp_q, freq_lim=f_lim, ylim=-120,title="Quantized + sampled signal")