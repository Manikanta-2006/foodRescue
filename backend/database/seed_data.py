import sys
import os
from datetime import datetime, timezone, timedelta
from werkzeug.security import generate_password_hash
from bson import ObjectId

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_db

def seed_database():
    db = get_db()
    print(f"🌱 Seeding sample data into '{db.name}'...")

    # Clear existing data
    db.users.delete_many({})
    db.organizations.delete_many({})
    db.donations.delete_many({})
    db.donation_requests.delete_many({})
    db.delivery_tasks.delete_many({})
    db.volunteer_profiles.delete_many({})

    now = datetime.now(timezone.utc)
    hashed_password = generate_password_hash("password123")

    # ==========================================================================
    # 1. USERS
    # ==========================================================================
    admin_id = ObjectId()
    donor1_id = ObjectId()
    donor2_id = ObjectId()
    donor3_id = ObjectId()
    ngo1_user_id = ObjectId()
    ngo2_user_id = ObjectId()
    ngo3_user_id = ObjectId()
    vol1_id = ObjectId()
    vol2_id = ObjectId()
    vol3_id = ObjectId()
    vol4_id = ObjectId()

    users = [
        {
            "_id": admin_id,
            "name": "Sarah Connor (Admin)",
            "email": "admin@foodrescue.org",
            "passwordHash": hashed_password,
            "role": "admin",
            "phone": "+1-555-0100",
            "address": "100 Civic Center Plaza, Metro City",
            "createdAt": now - timedelta(days=60),
            "isActive": True
        },
        # Donors
        {
            "_id": donor1_id,
            "name": "Fresh Bites Bistro",
            "email": "donor1@freshbites.com",
            "passwordHash": hashed_password,
            "role": "donor",
            "phone": "+1-555-0101",
            "address": "142 Market Street, Downtown",
            "createdAt": now - timedelta(days=45),
            "isActive": True
        },
        {
            "_id": donor2_id,
            "name": "Campus Central Dining",
            "email": "donor2@campusdining.edu",
            "passwordHash": hashed_password,
            "role": "donor",
            "phone": "+1-555-0102",
            "address": "800 University Way, West Campus",
            "createdAt": now - timedelta(days=30),
            "isActive": True
        },
        {
            "_id": donor3_id,
            "name": "Artisan Crust Bakery",
            "email": "donor3@artisanbakery.com",
            "passwordHash": hashed_password,
            "role": "donor",
            "phone": "+1-555-0103",
            "address": "55 Baker Lane, Old Town",
            "createdAt": now - timedelta(days=20),
            "isActive": True
        },
        # NGOs
        {
            "_id": ngo1_user_id,
            "name": "Hope Community Kitchen",
            "email": "ngo1@hopekitchen.org",
            "passwordHash": hashed_password,
            "role": "ngo",
            "phone": "+1-555-0201",
            "address": "312 Shelter Ave, East District",
            "createdAt": now - timedelta(days=40),
            "isActive": True
        },
        {
            "_id": ngo2_user_id,
            "name": "City Night Shelter",
            "email": "ngo2@cityshelter.org",
            "passwordHash": hashed_password,
            "role": "ngo",
            "phone": "+1-555-0202",
            "address": "77 Beacon Street, Southside",
            "createdAt": now - timedelta(days=25),
            "isActive": True
        },
        {
            "_id": ngo3_user_id,
            "name": "Youth Outreach Haven",
            "email": "ngo3@youthcare.org",
            "passwordHash": hashed_password,
            "role": "ngo",
            "phone": "+1-555-0203",
            "address": "404 North Boulevard, North District",
            "createdAt": now - timedelta(days=5),
            "isActive": True
        },
        # Volunteers
        {
            "_id": vol1_id,
            "name": "Alex Rivera",
            "email": "volunteer1@foodrescue.org",
            "passwordHash": hashed_password,
            "role": "volunteer",
            "phone": "+1-555-0301",
            "address": "22 Oak Ridge Lane, Midtown",
            "createdAt": now - timedelta(days=35),
            "isActive": True
        },
        {
            "_id": vol2_id,
            "name": "Sam Chen",
            "email": "volunteer2@foodrescue.org",
            "passwordHash": hashed_password,
            "role": "volunteer",
            "phone": "+1-555-0302",
            "address": "89 Pine Street, Downtown",
            "createdAt": now - timedelta(days=25),
            "isActive": True
        },
        {
            "_id": vol3_id,
            "name": "Jordan Taylor",
            "email": "volunteer3@foodrescue.org",
            "passwordHash": hashed_password,
            "role": "volunteer",
            "phone": "+1-555-0303",
            "address": "504 Maple Avenue, Westside",
            "createdAt": now - timedelta(days=15),
            "isActive": True
        },
        {
            "_id": vol4_id,
            "name": "Morgan Davis",
            "email": "volunteer4@foodrescue.org",
            "passwordHash": hashed_password,
            "role": "volunteer",
            "phone": "+1-555-0304",
            "address": "12 Harbor View, East District",
            "createdAt": now - timedelta(days=3),
            "isActive": True
        }
    ]
    db.users.insert_many(users)
    print(f"  ✅ Inserted {len(users)} users.")

    # ==========================================================================
    # 2. ORGANIZATIONS
    # ==========================================================================
    ngo1_org_id = ObjectId()
    ngo2_org_id = ObjectId()
    ngo3_org_id = ObjectId()

    organizations = [
        {
            "_id": ngo1_org_id,
            "userId": ngo1_user_id,
            "organizationName": "Hope Community Kitchen",
            "organizationType": "Community Kitchen & Food Pantry",
            "serviceArea": "East District & Metro Central",
            "verificationStatus": "verified",
            "createdAt": now - timedelta(days=40)
        },
        {
            "_id": ngo2_org_id,
            "userId": ngo2_user_id,
            "organizationName": "City Night Shelter",
            "organizationType": "Emergency Homeless Shelter",
            "serviceArea": "Southside & Downtown",
            "verificationStatus": "verified",
            "createdAt": now - timedelta(days=25)
        },
        {
            "_id": ngo3_org_id,
            "userId": ngo3_user_id,
            "organizationName": "Youth Outreach Haven",
            "organizationType": "Youth Support Center",
            "serviceArea": "North District",
            "verificationStatus": "pending",
            "createdAt": now - timedelta(days=5)
        }
    ]
    db.organizations.insert_many(organizations)
    print(f"  ✅ Inserted {len(organizations)} organizations.")

    # ==========================================================================
    # 3. VOLUNTEER PROFILES
    # ==========================================================================
    volunteer_profiles = [
        {
            "userId": vol1_id,
            "serviceArea": "Downtown & East District",
            "availability": "available",
            "transportType": "car",
            "transportCapacityKg": 50.0,
            "totalDeliveries": 8,
            "totalFoodDeliveredKg": 165.0,
            "totalPoints": 240,
            "badges": ["First Rescue", "Hunger Hero", "Super Courier", "Century Rescuer"],
            "createdAt": now - timedelta(days=35)
        },
        {
            "userId": vol2_id,
            "serviceArea": "Downtown & Southside",
            "availability": "busy",
            "transportType": "motorcycle",
            "transportCapacityKg": 25.0,
            "totalDeliveries": 5,
            "totalFoodDeliveredKg": 82.5,
            "totalPoints": 150,
            "badges": ["First Rescue", "Hunger Hero"],
            "createdAt": now - timedelta(days=25)
        },
        {
            "userId": vol3_id,
            "serviceArea": "Westside & Campus",
            "availability": "available",
            "transportType": "bicycle",
            "transportCapacityKg": 15.0,
            "totalDeliveries": 2,
            "totalFoodDeliveredKg": 24.0,
            "totalPoints": 60,
            "badges": ["First Rescue"],
            "createdAt": now - timedelta(days=15)
        },
        {
            "userId": vol4_id,
            "serviceArea": "Metro Wide",
            "availability": "available",
            "transportType": "van",
            "transportCapacityKg": 150.0,
            "totalDeliveries": 0,
            "totalFoodDeliveredKg": 0.0,
            "totalPoints": 0,
            "badges": [],
            "createdAt": now - timedelta(days=3)
        }
    ]
    db.volunteer_profiles.insert_many(volunteer_profiles)
    print(f"  ✅ Inserted {len(volunteer_profiles)} volunteer profiles.")

    # ==========================================================================
    # 4. COMPLETED HISTORICAL DONATIONS & DELIVERIES (Rescued Food)
    # ==========================================================================
    h_donations = [
        {
            "_id": ObjectId(),
            "donorId": donor1_id,
            "foodName": "Fresh Mediterranean Vegetable Bowls",
            "category": "Cooked Meals",
            "quantityKg": 25.0,
            "preparedAt": now - timedelta(days=12, hours=3),
            "availableUntil": now - timedelta(days=11, hours=20),
            "pickupAddress": "142 Market Street, Downtown",
            "dietaryInfo": ["Vegetarian", "Gluten-Free"],
            "description": "50 packed lunch containers of roast veggies, hummus, and quinoa.",
            "status": "delivered",
            "createdAt": now - timedelta(days=12, hours=4),
            "updatedAt": now - timedelta(days=12)
        },
        {
            "_id": ObjectId(),
            "donorId": donor3_id,
            "foodName": "Artisan Sourdough & Baguettes",
            "category": "Bakery & Bread",
            "quantityKg": 18.5,
            "preparedAt": now - timedelta(days=8, hours=5),
            "availableUntil": now - timedelta(days=7),
            "pickupAddress": "55 Baker Lane, Old Town",
            "dietaryInfo": ["Vegetarian", "Dairy-Free"],
            "description": "Surplus freshly baked sourdough boules and crispy whole-grain baguettes.",
            "status": "delivered",
            "createdAt": now - timedelta(days=8, hours=6),
            "updatedAt": now - timedelta(days=8, hours=1)
        },
        {
            "_id": ObjectId(),
            "donorId": donor2_id,
            "foodName": "Crisp Farm Apples & Organic Carrots",
            "category": "Fresh Produce",
            "quantityKg": 40.0,
            "preparedAt": now - timedelta(days=5, hours=2),
            "availableUntil": now - timedelta(days=3),
            "pickupAddress": "800 University Way, West Campus",
            "dietaryInfo": ["Vegan", "Organic"],
            "description": "Fresh, unbruised fruit and root vegetables packed in 4 sturdy crates.",
            "status": "delivered",
            "createdAt": now - timedelta(days=5, hours=3),
            "updatedAt": now - timedelta(days=5)
        },
        {
            "_id": ObjectId(),
            "donorId": donor1_id,
            "foodName": "Greek Yogurt & Pasteurized Milk",
            "category": "Dairy Products",
            "quantityKg": 15.0,
            "preparedAt": now - timedelta(days=2, hours=8),
            "availableUntil": now - timedelta(days=1, hours=12),
            "pickupAddress": "142 Market Street, Downtown",
            "dietaryInfo": ["Contains Dairy", "Vegetarian"],
            "description": "Chilled sealed dairy cartons kept refrigerated at 3°C.",
            "status": "delivered",
            "createdAt": now - timedelta(days=2, hours=9),
            "updatedAt": now - timedelta(days=2, hours=4)
        }
    ]
    db.donations.insert_many(h_donations)

    # Insert corresponding requests & delivery tasks for historical rescues
    vols = [vol1_id, vol2_id, vol1_id, vol3_id]
    ngos = [ngo1_org_id, ngo2_org_id, ngo1_org_id, ngo2_org_id]

    for idx, d in enumerate(h_donations):
        req_id = ObjectId()
        db.donation_requests.insert_one({
            "_id": req_id,
            "donationId": d["_id"],
            "organizationId": ngos[idx],
            "requestedQuantityKg": d["quantityKg"],
            "status": "fulfilled",
            "requestedAt": d["createdAt"] + timedelta(minutes=20),
            "reviewedAt": d["createdAt"] + timedelta(minutes=45)
        })

        db.delivery_tasks.insert_one({
            "_id": ObjectId(),
            "donationId": d["_id"],
            "requestId": req_id,
            "volunteerId": vols[idx],
            "status": "delivered",
            "pickedUpAt": d["createdAt"] + timedelta(hours=1),
            "deliveredAt": d["createdAt"] + timedelta(hours=2),
            "foodQuantityKg": d["quantityKg"],
            "pointsAwarded": True,
            "createdAt": d["createdAt"] + timedelta(minutes=50)
        })

    # ==========================================================================
    # 5. ACTIVE & IN-PROGRESS DONATIONS
    # ==========================================================================
    # A) In-progress donation: Picked up by Vol 1, en route to Hope Kitchen
    ip_don1_id = ObjectId()
    ip_req1_id = ObjectId()
    db.donations.insert_one({
        "_id": ip_don1_id,
        "donorId": donor1_id,
        "foodName": "Gourmet Sandwiches & Pasta Salad",
        "category": "Cooked Meals",
        "quantityKg": 16.0,
        "preparedAt": now - timedelta(hours=2),
        "availableUntil": now + timedelta(hours=6),
        "pickupAddress": "142 Market Street, Downtown",
        "dietaryInfo": ["Vegetarian Options", "Nut-Free"],
        "description": "Individually wrapped roast vegetable and cheese focaccias.",
        "status": "picked_up",
        "createdAt": now - timedelta(hours=3),
        "updatedAt": now - timedelta(minutes=30)
    })
    db.donation_requests.insert_one({
        "_id": ip_req1_id,
        "donationId": ip_don1_id,
        "organizationId": ngo1_org_id,
        "requestedQuantityKg": 16.0,
        "status": "approved",
        "requestedAt": now - timedelta(hours=2, minutes=30),
        "reviewedAt": now - timedelta(hours=2)
    })
    db.delivery_tasks.insert_one({
        "_id": ObjectId(),
        "donationId": ip_don1_id,
        "requestId": ip_req1_id,
        "volunteerId": vol1_id,
        "status": "picked_up",
        "pickedUpAt": now - timedelta(minutes=30),
        "deliveredAt": None,
        "foodQuantityKg": 16.0,
        "pointsAwarded": False,
        "createdAt": now - timedelta(hours=1, minutes=45)
    })

    # B) In-progress donation: Accepted by Vol 2, volunteer en route to pickup
    ip_don2_id = ObjectId()
    ip_req2_id = ObjectId()
    db.donations.insert_one({
        "_id": ip_don2_id,
        "donorId": donor2_id,
        "foodName": "Steamed Rice & Lentil Curry",
        "category": "Cooked Meals",
        "quantityKg": 22.0,
        "preparedAt": now - timedelta(hours=1),
        "availableUntil": now + timedelta(hours=5),
        "pickupAddress": "800 University Way, West Campus",
        "dietaryInfo": ["Vegan", "Gluten-Free", "Halal"],
        "description": "Hot insulated food warmers filled with freshly prepared dal and basmati rice.",
        "status": "assigned",
        "createdAt": now - timedelta(hours=2),
        "updatedAt": now - timedelta(minutes=15)
    })
    db.donation_requests.insert_one({
        "_id": ip_req2_id,
        "donationId": ip_don2_id,
        "organizationId": ngo2_org_id,
        "requestedQuantityKg": 22.0,
        "status": "approved",
        "requestedAt": now - timedelta(hours=1, minutes=30),
        "reviewedAt": now - timedelta(hours=1)
    })
    db.delivery_tasks.insert_one({
        "_id": ObjectId(),
        "donationId": ip_don2_id,
        "requestId": ip_req2_id,
        "volunteerId": vol2_id,
        "status": "accepted",
        "pickedUpAt": None,
        "deliveredAt": None,
        "foodQuantityKg": 22.0,
        "pointsAwarded": False,
        "createdAt": now - timedelta(minutes=40)
    })

    # C) Donation requested by NGO, waiting for Volunteer (pending assignment)
    ip_don3_id = ObjectId()
    ip_req3_id = ObjectId()
    db.donations.insert_one({
        "_id": ip_don3_id,
        "donorId": donor3_id,
        "foodName": "Fresh Butter Croissants & Brioche",
        "category": "Bakery & Bread",
        "quantityKg": 14.0,
        "preparedAt": now - timedelta(hours=3),
        "availableUntil": now + timedelta(hours=10),
        "pickupAddress": "55 Baker Lane, Old Town",
        "dietaryInfo": ["Vegetarian"],
        "description": "Unsold morning batch of premium pastries in bakery carry boxes.",
        "status": "requested",
        "createdAt": now - timedelta(hours=3),
        "updatedAt": now - timedelta(hours=1)
    })
    db.donation_requests.insert_one({
        "_id": ip_req3_id,
        "donationId": ip_don3_id,
        "organizationId": ngo1_org_id,
        "requestedQuantityKg": 14.0,
        "status": "approved",
        "requestedAt": now - timedelta(hours=2),
        "reviewedAt": now - timedelta(hours=1, minutes=30)
    })
    db.delivery_tasks.insert_one({
        "_id": ObjectId(),
        "donationId": ip_don3_id,
        "requestId": ip_req3_id,
        "volunteerId": None,
        "status": "pending_assignment",
        "pickedUpAt": None,
        "deliveredAt": None,
        "foodQuantityKg": 14.0,
        "pointsAwarded": False,
        "createdAt": now - timedelta(hours=1, minutes=30)
    })

    # ==========================================================================
    # 6. AVAILABLE DONATIONS (Open for NGO requests)
    # ==========================================================================
    available_donations = [
        {
            "donorId": donor2_id,
            "foodName": "Organic Mixed Greens & Bell Peppers",
            "category": "Fresh Produce",
            "quantityKg": 32.0,
            "preparedAt": now - timedelta(hours=4),
            "availableUntil": now + timedelta(days=2),
            "pickupAddress": "800 University Way, West Campus",
            "dietaryInfo": ["Vegan", "Organic"],
            "description": "Crisp salad greens, spinach, and red/yellow bell peppers from agriculture greenhouse.",
            "status": "available",
            "createdAt": now - timedelta(hours=4),
            "updatedAt": now - timedelta(hours=4)
        },
        {
            "donorId": donor1_id,
            "foodName": "Packaged Whole Grain Penne & Tomato Sauce",
            "category": "Packaged Goods",
            "quantityKg": 50.0,
            "preparedAt": now - timedelta(days=1),
            "availableUntil": now + timedelta(days=14),
            "pickupAddress": "142 Market Street, Downtown",
            "dietaryInfo": ["Vegetarian", "Shelf-Stable"],
            "description": "Sealed commercial food service cases of pasta and canned crushed plum tomatoes.",
            "status": "available",
            "createdAt": now - timedelta(hours=5),
            "updatedAt": now - timedelta(hours=5)
        },
        {
            "donorId": donor3_id,
            "foodName": "Artisanal Multigrain Loaves & Muffins",
            "category": "Bakery & Bread",
            "quantityKg": 12.0,
            "preparedAt": now - timedelta(hours=2),
            "availableUntil": now + timedelta(hours=18),
            "pickupAddress": "55 Baker Lane, Old Town",
            "dietaryInfo": ["Vegetarian", "Nut-Free"],
            "description": "High fiber loaf loaves and blueberry bran muffins.",
            "status": "available",
            "createdAt": now - timedelta(hours=2),
            "updatedAt": now - timedelta(hours=2)
        },
        {
            "donorId": donor1_id,
            "foodName": "Fresh Fruit Juices & Cold Brew Coffee",
            "category": "Beverages",
            "quantityKg": 20.0,
            "preparedAt": now - timedelta(hours=6),
            "availableUntil": now + timedelta(days=1),
            "pickupAddress": "142 Market Street, Downtown",
            "dietaryInfo": ["Vegan", "Gluten-Free"],
            "description": "Sealed bottles of cold-pressed orange and green juices kept chilled.",
            "status": "available",
            "createdAt": now - timedelta(hours=6),
            "updatedAt": now - timedelta(hours=6)
        }
    ]
    db.donations.insert_many(available_donations)

    print(f"  ✅ Inserted {len(h_donations) + 3 + len(available_donations)} total donations.")
    print(f"  ✅ Inserted donation requests and delivery tasks.")
    print(f"\n🎉 Database '{db.name}' successfully seeded with realistic sample data!")

if __name__ == "__main__":
    seed_database()
