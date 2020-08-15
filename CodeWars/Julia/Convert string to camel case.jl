function tocamelcase(str)
	result = ""
	skip = false 

	for i = 1:length(str)
		if (str[i] == '-' || str[i] == '_')
			result *= uppercase(str[i + 1])
			skip = true

		elseif (skip)
			skip = false
			continue
			
		else 
			result *= str[i]
			
		end
	end

	return result
end 