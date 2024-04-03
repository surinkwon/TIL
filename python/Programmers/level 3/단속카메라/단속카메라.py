def solution(routes):
    routes.sort(key = lambda x : (x[0], -x[1]))
    camera = [routes[0]]
    
    for i in range(1, len(routes)):
        [car_start, car_end] = routes[i]
        [camera_start, camera_end] = camera[-1]
        
        if camera_start <= car_start <= camera_end:
            camera_start = max(camera_start, car_start)
        else:
            camera.append(routes[i])
            continue
        
        if camera_end > car_end:
            camera_end = car_end
        camera[-1] = [camera_start, camera_end]

    return len(camera)