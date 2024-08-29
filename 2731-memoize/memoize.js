/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(func){
    let cache={}
    return function(...args){
        // let n=args[0]
        let n=JSON.stringify(args)
        if(n in cache){
            return cache[n];
        }else{
            // let result=func(n);
            let result=func.apply(this, args)
            cache[n]=result;
            return result;
        }
    }
 }


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

//  function square(n){
//     return n*n;
//  }

//  function memoize(func){
//     let cache={}
//     return function(...args){
//         let n=args[0]
//         if(n in cache){
//             return cache[n];
//         }else{
//             let res=func(n);
//             cache[n]=result;
//             return result;
//         }
//     }
//  }

// console.time()
// let effresult=memoize(square);
// console.log(effresult(5));
// console.timeEnd()

// console.time()

// console.log(effresult(5));
// console.timeEnd()