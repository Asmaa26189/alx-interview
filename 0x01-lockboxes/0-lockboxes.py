#!/usr/bin/python3
"""puzzle """


def lookNextOpenedBox(openBoxes):
    """lookNextOpenedBox"""
    for index, box in openBoxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('k')
    return None


def canUnlockAll(boxes):
    """canUnlockAll"""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    a = {}
    while True:
        if len(a) == 0:
            a[0] = {
                'status': 'opened',
                'k': boxes[0],
            }
        k = lookNextOpenedBox(a)
        if k:
            for key in k:
                try:
                    if a.get(key) and a.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    a[key] = {
                        'status': 'opened',
                        'k': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in a.values()]:
            continue
        elif len(a) == len(boxes):
            break
        else:
            return False

    return len(a) == len(boxes)


def main():
    """main"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()