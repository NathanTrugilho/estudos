clearvars;
close all;
count = 0;
number = 2;

fprintf('Os 4 primeiros números perfeitos são:\n');

while count < 4
    sumDivisors = 1;
    for i = 2:sqrt(number)
        if mod(number, i) == 0
            sumDivisors = sumDivisors + i;
            if i ~= number / i
                sumDivisors = sumDivisors + number / i;
            end
        end
    end

    if sumDivisors == number
        fprintf('%d\n', number);
        count = count + 1;
    end

    number = number + 1;
end
