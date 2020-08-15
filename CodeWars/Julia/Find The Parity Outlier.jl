function findoutlier(numbers)
    odd_count = 0
    even_count = 0
    last_odd = 0
    last_even = 0
    
    for n in numbers
        if (isodd(n))
            odd_count += 1
            last_odd = n
        
        else
            even_count += 1
            last_even = n

        end

        if (even_count + odd_count >= 3 && odd_count > 0 && even_count > 0)
            if (even_count - odd_count >= 1)
                return last_odd

            elseif (odd_count - even_count >= 1)
                return last_even

            end
        end
	end
end