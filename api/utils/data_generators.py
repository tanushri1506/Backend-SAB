import csv
from io import StringIO

from api.models import BranchRepresentative, Dupc, PhdDPPC, PhdSPPC, PhdCPPC

def handle_br(session):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Department", "Email"])

    data = BranchRepresentative.objects.filter(tenure=session)

    for obj in data:
        writer.writerow([obj.name, obj.post, obj.email])

    return output.getvalue()

def handle_dupc(session):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Department", "Email"])

    data = Dupc.objects.filter(tenure=session)

    for obj in data:
        writer.writerow([obj.name, obj.post, obj.email])

    return output.getvalue()

def handle_dppc(session):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Department", "Email"])

    # data = Dupc.objects.filter(tenure=session)
    data = PhdDPPC.objects.all() 

    for obj in data:
        writer.writerow([obj.name, obj.post, obj.email])

    return output.getvalue()

def handle_sppc(session):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Department", "Email"])

    # data = Dupc.objects.filter(tenure=session)
    data = PhdSPPC.objects.all() 

    for obj in data:
        writer.writerow([obj.name, obj.post, obj.email])

    return output.getvalue()

def handle_cppc(session):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Department", "Email"])

    # data = Dupc.objects.filter(tenure=session)
    data = PhdCPPC.objects.all() 

    for obj in data:
        writer.writerow([obj.name, obj.post, obj.email])

    return output.getvalue()




DATA_HANDLERS = {
    "BR": handle_br,
    "DUPC": handle_dupc,
    "DPPC": handle_dppc,
    "SPPC": handle_sppc,
    "CPPC": handle_cppc,
}