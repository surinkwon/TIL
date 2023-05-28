function solution(orders, course) {
    let answer = []
    const candidate = {}
    
    // 후보군 배열에 코스요리 구성 단품메뉴 개수 등록
    for (let i = 0; i < course.length; i += 1) {
        candidate[course[i]] = {}
    }
    
    /**
     * 코스요리 후보를 만드는 함수
     * @param {number} start 코스요리에 추가할 요리 인덱스
     * @param {Array} dishes 새로 만들어진 코스요리
     * @param {string} order 손님이 주문한 메뉴들
     * @param {number} num 만들고 있는 코스요리에 들어갈 단품메뉴 개수
     */
    function makeCourse(start, dishes, order, num) {
        if (dishes.length === num) {
            const newCourse = dishes.sort().join('')
            if (candidate[num][newCourse]) {
                candidate[num][newCourse] += 1
            } else {
                candidate[num][newCourse] = 1
            }
        } else {
            for (let i = start; i < order.length; i += 1) {
                makeCourse(i + 1, [...dishes, order[i]], order, num)
            }
        }
    }
    
    // 손님이 주문한 내역을 통해 코스요리가 될 수 있는 메뉴 후보 만들기
    // 각 후보가 나오는 횟수 저장
    for (const order of orders) {
        for (let courseNum = 0; courseNum < course.length; courseNum += 1) {
            if (order.length >= course[courseNum]) {
                makeCourse(0, [], order, course[courseNum])
            } else {
                break
            }
        }
    }
    
    // 후보군으로 실제 코스요리 구성하기
    for (const newCourses in candidate) {
        let maxOrder = 2
        let courses = []

        for (const newCourse in candidate[newCourses]) {
            if (candidate[newCourses][newCourse] > maxOrder) {
                maxOrder = candidate[newCourses][newCourse]
                courses = [newCourse]
            } else if (candidate[newCourses][newCourse] === maxOrder) {
                courses.push(newCourse)
            }
        }
        
        answer = [...answer, ...courses]
    }
    
    // 후보 이름순 정렬
    answer.sort()
    
    return answer
}