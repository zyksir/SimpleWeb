def remove_extras(lst):
    removed = []
    for e in lst:
       if e not in lst:
          removed.append(e)
    return removed
