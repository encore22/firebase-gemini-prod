import random
import string

# Function to generate a Luhn-valid IMEI

def generate_imei():
    def luhn_check(num):
        total = 0
        reverse_digits = num[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    while True:
        imei = ''.join(random.choices(string.digits, k=15))
        if luhn_check(imei):
            return imei

# Function to generate a random Android ID

def generate_android_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

# Function to generate a random serial number

def generate_serial_number():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

# Function to generate a build fingerprint for a Pixel 10 Pro

def generate_build_fingerprint():
    return "google/pixel_10_pro/pixel_10_pro:16/OPR3.170620.012/8188454:user/release-keys"

# Function to generate a random user agent for Pixel 10 Pro

def generate_user_agent():
    return "Mozilla/5.0 (Linux; Android 16; Pixel 10 Pro Build/OPR3.170620.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"

# Example usage
if __name__ == '__main__':
    print('Generated IMEI:', generate_imei())
    print('Generated Android ID:', generate_android_id())
    print('Generated Serial Number:', generate_serial_number())
    print('Generated Build Fingerprint:', generate_build_fingerprint())
    print('Generated User Agent:', generate_user_agent())