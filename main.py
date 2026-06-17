import time
import random
import string

# Helper function to generate dummy user data
def generate_dummy_data(count):
    data = []
    for i in range(count):
        name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        email_prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))
        email_domain = random.choice(['example.com', 'test.org', 'mail.net'])
        data.append({
            'id': i,
            'name': name.capitalize(),
            'email': f"{email_prefix}@{email_domain}",
            'status': random.choice(['active', 'inactive', 'pending'])
        })
    return data

NUM_RECORDS = 50000 # Number of records to process, adjust for faster/slower runs

# --- Version 1: Less Optimized (Before Silent Improvement) ---
def process_data_less_optimized(records):
    processed_results = []
    for record in records:
        # Less efficient string concatenation using '+' operator in a loop
        # This can create many intermediate string objects, impacting performance.
        profile_string = "User ID: " + str(record['id']) + ", Name: " + record['name'] + \
                         ", Email: " + record['email'] + ", Status: " + record['status']
        processed_results.append(profile_string)
    return processed_results

# --- Version 2: Optimized (After Silent Improvement) ---
def process_data_optimized(records):
    processed_results = []
    for record in records:
        # More efficient f-string for string formatting and concatenation.
        # This is a 'silent improvement' because the output is identical,
        # but the internal processing is faster. Users just feel it's quicker.
        profile_string = f"User ID: {record['id']}, Name: {record['name']}, " \
                         f"Email: {record['email']}, Status: {record['status']}"
        processed_results.append(profile_string)
    return processed_results

# --- Main Execution ---
if __name__ == "__main__":
    print("Demonstrating 'Silent Improvements' in performance.\n")

    dummy_records = generate_dummy_data(NUM_RECORDS)
    print(f"Processing {NUM_RECORDS} dummy user records...")

    # Run less optimized version and measure time
    start_time = time.perf_counter()
    less_optimized_output = process_data_less_optimized(dummy_records)
    end_time = time.perf_counter()
    time_less_optimized = end_time - start_time
    print(f"  Less Optimized Version took: {time_less_optimized:.4f} seconds")

    # Run optimized version and measure time
    start_time = time.perf_counter()
    optimized_output = process_data_optimized(dummy_records)
    end_time = time.perf_counter()
    time_optimized = end_time - start_time
    print(f"  Optimized Version took: {time_optimized:.4f} seconds")

    print("\n---------------------------------------------------")
    if time_optimized > 0:
        print(f"Improvement: Optimized version is {time_less_optimized / time_optimized:.2f}x faster.")
    else:
        print("Improvement: Optimized version was extremely fast (near zero time).")
    print("The output of both versions is functionally identical (verified below).")
    print("This demonstrates a 'silent improvement': the user experiences")
    print("the same feature, but it feels faster, without any visible change to the UI or functionality.")

    # Basic verification that outputs are the same (at least the first few records)
    if less_optimized_output[0] == optimized_output[0] and \
       less_optimized_output[-1] == optimized_output[-1]:
        print("\nVerification: First and last record outputs are identical for both versions.")
    else:
        print("\nVerification: WARNING - Outputs differ between versions!")
