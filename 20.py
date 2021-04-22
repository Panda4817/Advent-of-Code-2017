import sys

def process_data(data):
    lines = data.split("\n")
    particles = {}
    n = 0
    for l in lines:
        particles[n] = {}
        pva = l.split(", ")
        for s in pva:
            particles[n][s[0]] = [int(i) for i in s[3:-1].split(",")]
        n += 1
    return particles, n

def calculate_md(p, particles):
    x = 0
    y = 1
    z = 2
    
    return abs(particles[p]['p'][x]) + abs(particles[p]['p'][y]) + abs(particles[p]['p'][z])

def update_particle(p, particles):
    x = 0
    y = 1
    z = 2

    # Increase the X velocity by the X acceleration.
    particles[p]['v'][x] += particles[p]['a'][x]
    # Increase the Y velocity by the Y acceleration.
    particles[p]['v'][y] += particles[p]['a'][y]
    # Increase the Z velocity by the Z acceleration.
    particles[p]['v'][z] += particles[p]['a'][z]
    # Increase the X position by the X velocity.
    particles[p]['p'][x] += particles[p]['v'][x]
    # Increase the Y position by the Y velocity.
    particles[p]['p'][y] += particles[p]['v'][y]
    # Increase the Z position by the Z velocity.
    particles[p]['p'][z] += particles[p]['v'][z]

    return particles[p]

def closest_particle(particles, total):
    lowest = sys.maxsize
    particle = None
    for p in range(total):
        md = calculate_md(p, particles)
        if md < lowest:
            particle = p
            lowest = md
    return particle
    

def part1(data):
    particles, total = process_data(data)
    close_particle = closest_particle(particles, total)

    ticks = 0
    while ticks <= total:
        for p in range(total):
            particles[p] = update_particle(p, particles)
        
        close_particle = closest_particle(particles, total)

        ticks += 1
    
    return close_particle

def resolve_collisions(particles, total):
    mark_to_remove = set()
    for p1 in particles.keys():
        for p2 in particles.keys():
            if p1 != p2 and particles[p1]['p'] == particles[p2]['p']:
                mark_to_remove.add(p1)
                mark_to_remove.add(p2)
    
    for p in mark_to_remove:
        del particles[p]
        total -= 1
    
    return particles, total


def part2(data):
    particles, total = process_data(data)
    particles, total = resolve_collisions(particles, total)
    ticks = 0
    while ticks <= total:
        for p in particles.keys():
            particles[p] = update_particle(p, particles)
        particles, total = resolve_collisions(particles, total)
        ticks += 1
    
    return len(particles.keys())