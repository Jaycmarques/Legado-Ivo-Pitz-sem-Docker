from django.core.management.base import BaseCommand
from familytree.models import FamilyMember, Relationship


class Command(BaseCommand):
    help = 'Populate family tree from TreeFromWebsite.txt'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the family data file')

    def handle(self, *args, **options):
        family = []
        file_path = options['file_path']  # Get the file path passed as argument
        try:
            with open(file_path) as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():  # Ignore empty lines
                        parts = line.strip().split(" - ")
                        
                        # Ensure there are at least 2 parts (ID and name)
                        if len(parts) >= 2:
                            id = parts[0]
                            name = parts[1]
                            info = parts[2][0].capitalize()+parts[2][1:] if len(parts) > 2 else ''  # Use empty string if no extra info
                        else:
                            self.stderr.write(self.style.ERROR(f"Invalid line format: {line.strip()}"))
                            continue

                        try:
                            # Try to find the FamilyMember by id
                            member = FamilyMember.objects.get(id=id)
                            # If found, update the relevant fields
                            member.name = name.upper()
                            member.info = info
                            member.save()
                        except FamilyMember.DoesNotExist:
                            # If not found, create a new FamilyMember
                            member = FamilyMember.objects.create(id=id, name=name.upper(), info=info)

                        family.append(member)

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error reading file: {str(e)}"))
            return

        for parent in family:
            parent_id = parent.id
            for child in family:
                child_id = child.id
                # Check if the child's ID starts with the parent's ID
                if child_id.startswith(f"{parent_id}."):
                    try:
                        # Extract the child number from the ID
                        child_number = int(child_id[len(parent_id) + 1:])
                        if child_number >= 1:
                            Relationship.objects.create(parent=parent, child=child)
                    except ValueError:
                        # If not a valid number, ignore the ID
                        continue

        self.stdout.write(self.style.SUCCESS('Successfully populated family tree'))
