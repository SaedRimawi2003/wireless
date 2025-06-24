def calculate_wireless_blocks(data):
    # Sampler output: samples/sec
    sampler_output = data.sampling_rate_hz

    # Quantizer: bits/sec = samples/sec × bits/sample
    quantizer_output = sampler_output * data.quantization_bits

    # Source Encoder: يقلل البيانات حسب النسبة
    source_encoder_output = quantizer_output * data.source_encoding_ratio

    # Channel Encoder: يزيد البيانات حسب الـ coding rate
    channel_encoder_output = source_encoder_output / data.channel_coding_rate

    # Interleaver: لا يغير الحجم
    interleaver_output = channel_encoder_output

    # Burst Formatter: نضيف مثلاً 5% كـ padding
    burst_formatter_output = interleaver_output * 1.05

    return {
        "sampler_output_rate": sampler_output,
        "quantizer_output_rate": quantizer_output,
        "source_encoder_output": source_encoder_output,
        "channel_encoder_output": channel_encoder_output,
        "interleaver_output": interleaver_output,
        "burst_formatter_output": burst_formatter_output
    }
