def calculate_wireless_blocks(data):
    # 1️⃣ Effective frequency: أصغر قيمة بين الـ bandwidth والـ cutoff frequency
    effective_freq = min(data.bandwidth_hz, data.cutoff_frequency_hz)

    # 2️⃣ Sampler output = 2 * effective frequency (Nyquist rate)
    sampler_output = 2 * effective_freq

    # 3️⃣ Quantization: Rate = Sampling_Rate × Bits_per_Sample
    quantizer_output = sampler_output * data.quantization_bits

    # 4️⃣ Source coding: Rate = Input_Rate × Coding_Rate
    source_encoder_output = quantizer_output * data.source_encoding_ratio

    # 5️⃣ Channel coding: Rate = Input_Rate / Coding_Rate
    channel_encoder_output = source_encoder_output / data.channel_coding_rate

    # 6️⃣ Interleaver: عادة لا يغير المعدل، نفس الـ channel encoder output
    interleaver_output = channel_encoder_output

    # 7️⃣ Overhead: Rate = Input_Rate × (1 + Overhead_Percentage / 100)
    overhead_output = interleaver_output * (1 + data.overhead_percentage / 100)

    # 8️⃣ Burst format: Rate = Overhead Rate
    burst_formatter_output = overhead_output

    return {
        "effective_frequency_hz": effective_freq,
        "sampler_output_rate": sampler_output,
        "quantizer_output_rate": quantizer_output,
        "source_encoder_output_rate": source_encoder_output,
        "channel_encoder_output_rate": channel_encoder_output,
        "interleaver_output_rate": interleaver_output,
        "overhead_output_rate": overhead_output,
        "burst_formatter_output_rate": burst_formatter_output
    }
