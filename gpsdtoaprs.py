import gpsd
try:
  gpsd.connect()
  pos = gpsd.get_current()
  pars = pos.position()
except UserWarning:
  print("ERROR: GPS is not active")
  pars = [0.00, 0.00]
def lat():
  final = pars[0] * 100
  final = "{:.2f}".format(final)
  if (float(final) < 0):
    final = final * -1
    final = str(final) + "S"
  else:
    final = str(final) + "N"
  return final
def lon():
  final = pars[1] * 100
  final = "{:.2f}".format(final)
  if (float(final) < 0):
    final = final * -1
    count = final
    final = str(final) + "W"
  else:
    count = final
    final = str(final) + "E"
  if (float(count) - 10000 < 0):
    final = str(0) + str(final)
  return final
print("GPSD: " + str(lat()) + ", " + str(lon()))
