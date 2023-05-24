function solution(number, k) {
    const stack = [Number(number[0])]
    
    for (let i = 1; i < number.length; i += 1) {
        const curNum = Number(number[i])
        
        while (stack.length > 0 && stack[stack.length - 1] < curNum && k > 0) {
            stack.pop()
            k -= 1
        }
        
        stack.push(curNum)
    }
    
    if (k) {
        stack.pop()
    }
    
    return stack.join('')
}