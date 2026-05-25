"""
Day 9 — OOP Part 1: Classes, Objects, Attributes, Methods
Practice File
"""

# ─── SECTION 1: What is a Class? ─────────────────────────────────────────────

# A class is a BLUEPRINT.
# An object is an INSTANCE of that blueprint.
#
# Real-world analogy:
# - A class is like the design document for a "Lead" in a CRM system.
# - Each actual lead (Priya, Rahul) is an object made from that blueprint.


class Lead:
    """Represents a sales lead in the CRM system."""

    company_name = "TechCorp CRM"    # class attribute — shared by all instances

    def __init__(self, name, company, score, revenue):
        """Initialise a new Lead object."""
        # instance attributes — unique to each object
        self.name = name
        self.company = company
        self.score = score
        self.revenue = revenue
        self.status = self._classify()   # set on creation

    def _classify(self):
        """Internal method to classify lead (prefix _ = private by convention)."""
        if self.score >= 85:
            return "Hot"
        elif self.score >= 70:
            return "Warm"
        elif self.score >= 50:
            return "Cold"
        return "Unqualified"

    def get_summary(self):
        """Return a formatted lead summary."""
        return (
            f"{'='*35}\n"
            f"Name    : {self.name}\n"
            f"Company : {self.company}\n"
            f"Score   : {self.score}/100\n"
            f"Revenue : ₹{self.revenue:,.0f}\n"
            f"Status  : {self.status}\n"
            f"{'='*35}"
        )

    def update_score(self, new_score):
        """Update the lead score and reclassify."""
        self.score = new_score
        self.status = self._classify()
        print(f"Score updated to {new_score} → Status: {self.status}")

    def __str__(self):
        """String representation — used when you print() the object."""
        return f"Lead({self.name}, {self.status}, Score={self.score})"


# ─── SECTION 2: Creating Objects ─────────────────────────────────────────────

lead1 = Lead("Priya Sharma", "Innovate Solutions", 87, 1250000)
lead2 = Lead("Rahul Verma", "DataDriven Corp", 65, 450000)
lead3 = Lead("Ankit Gupta", "CloudBase", 92, 2100000)

print(lead1.get_summary())
print(lead2.get_summary())
print(lead3)             # calls __str__


# ─── SECTION 3: Modifying Attributes ─────────────────────────────────────────

print("\n--- Score Update ---")
lead2.update_score(78)

# Access class attribute
print(f"\nCRM System: {Lead.company_name}")
print(f"Lead1 CRM : {lead1.company_name}")   # accessible from instances too


# ─── SECTION 4: Storing Objects in Lists ─────────────────────────────────────

print("\n--- CRM Pipeline ---")
pipeline = [lead1, lead2, lead3]

hot_leads = [l for l in pipeline if l.status == "Hot"]
print(f"Total leads : {len(pipeline)}")
print(f"Hot leads   : {len(hot_leads)}")

print("\nAll leads:")
for lead in sorted(pipeline, key=lambda l: l.score, reverse=True):
    print(f"  {lead}")
