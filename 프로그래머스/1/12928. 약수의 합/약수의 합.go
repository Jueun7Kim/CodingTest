func solution(n int) int {
    var x int;
    
    for i := 1; i <= n; i++{
        if n % i == 0{
            x += i
        }    
    }
    
    return x
} 