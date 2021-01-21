// Largest prime factor

fn main() {
    let mut number: i64 = 600851475143; 
    let mut prime_numbers = Vec::new();
    let mut candidate = 2;

    while number > 1 {
        while number % candidate == 0 {
            prime_numbers.push(candidate);
            number /= candidate;
        }

        candidate += 1;
    }

    println!("{:?}", prime_numbers);
}