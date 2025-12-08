
# -------------------------------------------------------------------
# Library Management System - Python, OOP, CRUD Operations, Streamlit
# -------------------------------------------------------------------

import json
import random
import string
from pathlib import Path
from datetime import datetime

import streamlit as st

# -----------------------
# Basic Config
# -----------------------
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

# Center text inside tables & metrics
st.markdown("""
<style>
thead tr th:first-child {text-align: center !important;}
tbody td {text-align: center !important;}
thead th {text-align: center !important;}
.stMetric { text-align: center !important; }
</style>
""", unsafe_allow_html=True)


DATABASE_PATH = Path("library.json")


# -----------------------
# Data Layer
# -----------------------
def init_data():
    """Initialize the JSON file if it doesn't exist."""
    if not DATABASE_PATH.exists():
        data = {"books": [], "members": []}
        save_data(data)


def load_data():
    """Load data from JSON file."""
    init_data()
    content = DATABASE_PATH.read_text().strip()
    if not content:
        return {"books": [], "members": []}
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"books": [], "members": []}
    # Ensure keys exist
    data.setdefault("books", [])
    data.setdefault("members", [])
    return data


def save_data(data):
    """Save data back to JSON file."""
    with open(DATABASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)


def gen_id(prefix="B"):
    """Generate random ID like B_ABCDE or M_123AB."""
    random_id = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return f"{prefix}_{random_id}"


def find_member(data, member_id):
    return next((m for m in data["members"] if m["id"] == member_id), None)


def find_book(data, book_id):
    return next((b for b in data["books"] if b["id"] == book_id), None)


# -----------------------
# UI Helper Functions
# -----------------------
def show_header():
    st.title("📚 Library Management System")
    st.caption("Interactive Library Management System showcasing Python, OOP, CRUD and Streamlit UI skills")


def show_dashboard(data):
    total_books = len(data["books"])
    total_members = len(data["members"])
    total_copies = sum(b.get("total_copies", 0) for b in data["books"])
    available_copies = sum(b.get("available_copies", 0) for b in data["books"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Book Titles", total_books)
    col2.metric("Total Members", total_members)
    col3.metric("Total Copies", total_copies)
    col4.metric("Available Copies", available_copies)

    st.markdown("---")
    st.subheader("Recent Books")
    if data["books"]:
        # Show last 5 added books
        sorted_books = sorted(
            data["books"],
            key=lambda x: x.get("added_on", ""),
            reverse=True
        )[:5]
        st.table(
            [
                {
                    "ID": b["id"],
                    "Title": b["title"],
                    "Author": b["author"],
                    "Total": b["total_copies"],
                    "Available": b["available_copies"],
                    "Added On": b.get("added_on", ""),
                }
                for b in sorted_books
            ]
        )
    else:
        st.info("No books found. Add some from the **Books** section.")


def page_books(data):
    st.subheader("📖 Manage Books")

    col1, col2 = st.columns([2, 1])

    # List books
    with col1:
        st.markdown("### All Books")
        if not data["books"]:
            st.warning("No books in the library yet.")
        else:
            search = st.text_input("Search by title or author", "")
            books = data["books"]
            if search:
                search_lower = search.lower()
                books = [
                    b for b in books
                    if search_lower in b["title"].lower()
                    or search_lower in b["author"].lower()
                ]

            st.dataframe(
                [
                    {
                        "ID": b["id"],
                        "Title": b["title"],
                        "Author": b["author"],
                        "Total Copies": b["total_copies"],
                        "Available": b["available_copies"],
                        "Added On": b.get("added_on", ""),
                    }
                    for b in books
                ],
                use_container_width=True,
            )

    # Add book form
    with col2:
        st.markdown("### ➕ Add New Book")
        with st.form("add_book_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Book Author")
            copies = st.number_input("Number of Copies", min_value=1, value=1, step=1)
            submit = st.form_submit_button("Add Book")

        if submit:
            if not title.strip() or not author.strip():
                st.error("Title and author are required.")
            else:
                new_book = {
                    "id": gen_id("B"),
                    "title": title.strip(),
                    "author": author.strip(),
                    "total_copies": int(copies),
                    "available_copies": int(copies),
                    "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                data["books"].append(new_book)
                save_data(data)
                st.success(f"Book '{title}' added successfully!")


def page_members(data):
    st.subheader("🧑‍🤝‍🧑 Manage Members")

    col1, col2 = st.columns([2, 1])

    # List members
    with col1:
        st.markdown("### All Members")
        if not data["members"]:
            st.warning("No members yet.")
        else:
            search = st.text_input("Search by member name or email", key="member_search")
            members = data["members"]
            if search:
                lower = search.lower()
                members = [
                    m for m in members
                    if lower in m["name"].lower() or lower in m["email"].lower()
                ]

            st.dataframe(
                [
                    {
                        "ID": m["id"],
                        "Name": m["name"],
                        "Email": m["email"],
                        "Borrowed Count": len(m.get("borrowed", [])),
                    }
                    for m in members
                ],
                use_container_width=True,
            )

    # Add member form
    with col2:
        st.markdown("### ➕ Add Member")
        with st.form("add_member_form"):
            name = st.text_input("Member Name")
            email = st.text_input("Member Email")
            submit = st.form_submit_button("Add Member")

        if submit:
            if not name.strip() or not email.strip():
                st.error("Name and email are required.")
            else:
                new_member = {
                    "id": gen_id("M"),
                    "name": name.strip(),
                    "email": email.strip(),
                    "borrowed": [],
                }
                data["members"].append(new_member)
                save_data(data)
                st.success(f"Member '{name}' added successfully!")


def page_borrow_return(data):
    st.subheader("📦 Borrow & 🔁 Return Books")

    col1, col2 = st.columns(2)

    # ---------- Borrow Book ----------
    with col1:
        st.markdown("### 📦 Borrow Book")

        if not data["members"]:
            st.info("No members available. Please add a member first.")
        elif not data["books"]:
            st.info("No books available. Please add a book first.")
        else:
            # Filter books that have available copies
            available_books = [b for b in data["books"] if b["available_copies"] > 0]

            if not available_books:
                st.warning("No books with available copies.")
            else:
                member_options = {f"{m['name']} ({m['id']})": m["id"] for m in data["members"]}
                selected_member_label = st.selectbox("Select Member", list(member_options.keys()))
                selected_member_id = member_options[selected_member_label]
                member = find_member(data, selected_member_id)

                book_options = {
                    f"{b['title']} by {b['author']} [{b['available_copies']} available] ({b['id']})": b["id"]
                    for b in available_books
                }
                selected_book_label = st.selectbox("Select Book to Borrow", list(book_options.keys()))
                selected_book_id = book_options[selected_book_label]
                book = find_book(data, selected_book_id)

                if st.button("Borrow Book"):
                    if member is None or book is None:
                        st.error("Invalid member or book selection.")
                    else:
                        borrow_entry = {
                            "book_id": book["id"],
                            "title": book["title"],
                            "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                        member.setdefault("borrowed", []).append(borrow_entry)
                        book["available_copies"] -= 1
                        save_data(data)
                        st.success(f"'{book['title']}' borrowed by {member['name']}.")

    # ---------- Return Book ----------
    with col2:
        st.markdown("### 🔁 Return Book")

        if not data["members"]:
            st.info("No members available.")
        else:
            member_options = {f"{m['name']} ({m['id']})": m["id"] for m in data["members"]}
            selected_member_label_ret = st.selectbox(
                "Select Member (for return)", list(member_options.keys()), key="ret_member"
            )
            selected_member_id_ret = member_options[selected_member_label_ret]
            member_ret = find_member(data, selected_member_id_ret)

            borrowed_list = member_ret.get("borrowed", [])
            if not borrowed_list:
                st.warning("This member has no borrowed books.")
            else:
                borrowed_options = {
                    f"{i+1}. {b['title']} ({b['book_id']}) on {b['borrow_on']}": i
                    for i, b in enumerate(borrowed_list)
                }
                selected_borrow_label = st.selectbox(
                    "Select Borrowed Book to Return",
                    list(borrowed_options.keys()),
                )
                selected_index = borrowed_options[selected_borrow_label]

                if st.button("Return Selected Book"):
                    try:
                        selected_entry = borrowed_list.pop(selected_index)
                        book = find_book(data, selected_entry["book_id"])
                        if book:
                            book["available_copies"] += 1
                        save_data(data)
                        st.success(f"Returned '{selected_entry['title']}' successfully.")
                    except Exception as e:
                        st.error(f"Error while returning book: {e}")


def page_raw_data(data):
    st.subheader("🔍 Raw JSON Data (Debug / Advanced)")
    st.json(data)


# -----------------------
# MAIN APP
# -----------------------
def main():
    data = load_data()
    show_header()

    menu = st.sidebar.radio(
        "Navigate",
        ["Dashboard", "Books", "Members", "Borrow / Return", "Raw Data"],
        index=0,
    )

    if menu == "Dashboard":
        show_dashboard(data)
    elif menu == "Books":
        page_books(data)
    elif menu == "Members":
        page_members(data)
    elif menu == "Borrow / Return":
        page_borrow_return(data)
    elif menu == "Raw Data":
        page_raw_data(data)


if __name__ == "__main__":
    main()
