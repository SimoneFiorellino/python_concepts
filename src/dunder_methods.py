"""
Dunder methods (“double-underscore methods”) are special hooks that let
your class integrate seamlessly with Python's built-in behaviors.
They define how objects are created, compared, represented, called,
iterated over, used in operators, and much more. Python automatically
invokes these methods in specific situations
"""

from __future__ import annotations
from functools import total_ordering
from typing import Any, Dict, Iterator, List, Tuple


@total_ordering  # adds automatically the other ordering methods
class Sorcerer:
    """
    A Sorcerer class that demonstrates many Python dunder methods.
    """

    # ------------------------------------------------------------------
    # Object creation & initialization
    # ------------------------------------------------------------------
    def __new__(cls, *args, **kwargs):
        # You almost never override __new__, but this shows when it's called.
        instance = super().__new__(cls)
        # You could customize instance creation here
        return instance

    def __init__(
        self, name: str, level: int, mana: int, spells: Dict[str, int] | None = None
    ):
        # NOTE: we use __setattr__ internally, so to avoid infinite recursion
        # we bypass it for the initial attributes using super().__setattr__
        # super() is referred to the parent class (object here)
        super().__setattr__("name", name)
        super().__setattr__("level", level)
        super().__setattr__("mana", mana)
        super().__setattr__("spells", spells or {})  # {spell_name: spell_level}

    # ------------------------------------------------------------------
    # String / representation API
    # ------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Unambiguous representation, used in the REPL and debugging.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"level={self.level}, mana={self.mana}, spells={list(self.spells.keys())!r})"
        )

    def __str__(self) -> str:
        """
        User-friendly, pretty string.
        """
        return f"Sorcerer {self.name} (Lv {self.level}, Mana {self.mana}, {len(self)} spells)"

    def __format__(self, format_spec: str) -> str:
        """
        Custom formatting support: format(sorcerer, "short") / f"{sorc:short}"
        """
        if format_spec == "short":
            return f"{self.name} (Lv {self.level})"
        elif format_spec == "mana":
            return f"{self.name}: {self.mana} MP"
        # Fallback to default string representation
        return format(str(self), format_spec)

    def __bytes__(self) -> bytes:
        """
        Example of bytes representation (totally arbitrary here).
        """
        return f"{self.name}|{self.level}|{self.mana}".encode("utf-8")

    # ------------------------------------------------------------------
    # Comparison & hashing
    # ------------------------------------------------------------------
    def __eq__(self, other: Any) -> bool:
        """
        Equality: two sorcerers are equal if name & level match.
        """
        if not isinstance(other, Sorcerer):
            return NotImplemented
        return (self.name, self.level) == (other.name, other.level)

    def __lt__(self, other: Any) -> bool:
        """
        Ordering: compare by level, then mana.
        total_ordering fills in >, <=, >= for us.
        """
        if not isinstance(other, Sorcerer):
            return NotImplemented
        return (self.level, self.mana) < (other.level, other.mana)

    def __hash__(self) -> int:
        """
        Makes the object usable as a dict key / in sets.
        """
        return hash((self.name, self.level))

    # ------------------------------------------------------------------
    # Boolean / length
    # ------------------------------------------------------------------
    def __bool__(self) -> bool:
        """
        Truthiness: a sorcerer is "truthy" if they have mana.
        """
        return self.mana > 0

    def __len__(self) -> int:
        """
        Length: number of known spells.
        """
        return len(self.spells)

    # ------------------------------------------------------------------
    # Iteration & container protocol
    # ------------------------------------------------------------------
    def __iter__(self) -> Iterator[Tuple[str, int]]:
        """
        Iterate over (spell_name, spell_level).
        If the class is an iterator then we implement __next__ as well.
        """
        return iter(self.spells.items())

    def __contains__(self, spell_name: object) -> bool:
        """
        `spell_name in sorcerer`
        """
        return spell_name in self.spells

    def __getitem__(self, spell_name: str) -> int:
        """
        Indexing: sorcerer["fireball"] -> level of the spell.
        """
        return self.spells[spell_name]

    def __setitem__(self, spell_name: str, spell_level: int) -> None:
        """
        Assignment: sorcerer["fireball"] = 3
        """
        self.spells[spell_name] = spell_level

    def __delitem__(self, spell_name: str) -> None:
        """
        Deletion: del sorcerer["fireball"]
        """
        del self.spells[spell_name]

    # ------------------------------------------------------------------
    # Numeric protocol (add sorcerers / mana)
    # ------------------------------------------------------------------
    def __add__(self, other: Any) -> Sorcerer:
        """
        sorcerer + int
        - add to mana.
        """
        if isinstance(other, int):
            # Return a new sorcerer with more mana
            return Sorcerer(
                name=self.name,
                level=self.level,
                mana=self.mana + other,
                spells=self.spells.copy(),
            )
        raise ValueError("Can only add mana to Sorcerer")

    def __sub__(self, other: Any) -> Sorcerer:
        """
        sorcerer - int
        - subtract from mana.
        """
        if isinstance(other, int):
            new_mana = max(0, self.mana - other)
            return Sorcerer(
                name=self.name,
                level=self.level,
                mana=new_mana,
                spells=self.spells.copy(),
            )
        raise ValueError("Can only subtract mana from Sorcerer")

    def __mul__(self, other: Any) -> Sorcerer:
        """
        sorcerer * other
        - If other is int, multiply mana.
        """
        if isinstance(other, int):
            return Sorcerer(
                name=self.name,
                level=self.level,
                mana=self.mana * other,
                spells=self.spells.copy(),
            )
        raise ValueError("Can only multiply Sorcerer by int")

    def __truediv__(self, other: Any) -> Sorcerer:
        """
        sorcerer / other
        - If other is int, divide mana.
        - We use // for integer division of mana.
        """
        if isinstance(other, int):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Sorcerer(
                name=self.name,
                level=self.level,
                mana=self.mana // other,
                spells=self.spells.copy(),
            )
        raise ValueError("Can only divide Sorcerer by int")

    def __radd__(self, other: Any) -> Sorcerer:
        """
        other + sorcerer (for int + sorcerer).
        """
        return self.__add__(other)

    def __iadd__(self, other: Any) -> Sorcerer:
        """
        In-place addition: sorcerer += X
        """
        if isinstance(other, int):
            self.mana += other
            return self
        raise ValueError("Can only add int to Sorcerer")

    # ------------------------------------------------------------------
    # Callable objects
    # ------------------------------------------------------------------
    def __call__(self, spell_name: str, target: str | None = None) -> str:
        """
        Make the instance callable: sorcerer("fireball", target="goblin")
        """
        if spell_name not in self.spells:
            return f"{self.name} doesn't know the spell '{spell_name}'."

        cost = self.spells[spell_name]
        if self.mana < cost:
            return f"{self.name} tries to cast '{spell_name}' but lacks mana!"

        self.mana -= cost
        if target is None:
            return f"{self.name} casts '{spell_name}' (cost {cost} MP). Remaining mana: {self.mana}."
        else:
            return (
                f"{self.name} casts '{spell_name}' on {target}! "
                f"(cost {cost} MP, remaining mana: {self.mana})"
            )

    # ------------------------------------------------------------------
    # Attribute access customisation
    # ------------------------------------------------------------------
    def __getattribute__(self, name: str) -> Any:
        """
        Intercepts *all* attribute access.
        Be very careful to avoid infinite recursion.
        """
        # Example: transparent alias "hp" -> "mana" just for fun
        if name == "hp":
            name = "mana"
        return super().__getattribute__(name)

    def __getattr__(self, name: str) -> Any:
        """
        Called *only* when normal attribute lookup fails.
        We'll use it to expose "num_spells" dynamically.
        """
        if name == "num_spells":
            return len(self.spells)
        raise AttributeError(f"{self.__class__.__name__!s} has no attribute {name!r}")

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Intercepts attribute assignment. Let's validate some fields.
        """
        if name == "level" and value < 1:
            raise ValueError("Sorcerer level must be >= 1")
        if name == "mana" and value < 0:
            raise ValueError("Mana cannot be negative")
        # Use default behavior for everything else
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """
        Intercepts attribute deletion.
        """
        if name in {"name", "level"}:
            raise AttributeError(f"Cannot delete core attribute {name!r}")
        super().__delattr__(name)

    # ------------------------------------------------------------------
    # Misc / introspection helpers (not dunders but handy)
    # ------------------------------------------------------------------
    def known_spells(self) -> List[str]:
        return list(self.spells.keys())


if __name__ == "__main__":
    print("\n========== SORCERER CLASS DEMO (VERBOSE) ==========\n")

    print(">>> Creating sorcerers s1 and s2...")
    s1 = Sorcerer(
        "Aelar", level=5, mana=20, spells={"fireball": 3, "shield": 1, "firebolt": 0}
    )
    s2 = Sorcerer(
        "Lyra",
        level=7,
        mana=30,
        spells={"fireshild": 4, "fireball": 3, "haste": 3, "firebolt": 0},
    )
    print("Created s1:", repr(s1))
    print("Created s2:", repr(s2))
    print()

    print("========== STRING REPRESENTATIONS ==========")
    print("repr(s1):", repr(s1))
    print("str(s1):", str(s1))
    print("formatted short:", f"{s1:short}")
    print("formatted mana:", f"{s1:mana}")
    print("bytes(s1):", bytes(s1))
    print()

    print("========== COMPARISON & HASHING ==========")
    print("s1 == s2:", s1 == s2)
    print("s1 < s2:", s1 < s2)
    print("hash(s1):", hash(s1))
    print("hash(s2):", hash(s2))
    print()

    print("========== CONTAINER & ITEM ACCESS ==========")
    print('Is "fireball" in s1?', "fireball" in s1)
    print('Is "fireball" in s2?', "fireball" in s2)
    print('s2["fireball"]:', s2["fireball"])

    print("\nAdding s1['misty_step'] = 2 ...")
    s1["misty_step"] = 2
    print("Now s1 spells:", s1.spells)

    print("Deleting s1['misty_step']...")
    del s1["misty_step"]
    print("Now s1 spells:", s1.spells)
    print()

    print("========== ITERATION ==========")
    print("Iterating over s2 spells:")
    for spell, level in s2:
        print("  Spell:", spell, "| Level:", level)
    print()

    print("========== NUMERIC OPERATIONS ==========")
    print("s3 = s1 + 10 (adds mana):")
    s3 = s1 + 10
    print("s3:", repr(s3))

    print("s1 * 2 (double mana):")
    print(repr(s1 * 2))

    print("s2 - 5 (subtract mana):")
    print(repr(s2 - 5))

    print("s2 / 2 (integer divide mana):")
    print(repr(s2 / 2))
    print()

    print("========== CALLABLE (CASTING SPELLS) ==========")
    print('s1("firebolt", target="goblin") →')
    print(" ", s1("firebolt", target="goblin"))
    print("Is s1 truthy (mana > 0)?", bool(s1))
    print("How many spells does s1 know? len(s1) =", len(s1))
    print()

    print("========== ATTRIBUTE MAGIC ==========")
    print("Accessing s1.hp (alias for mana):", s1.hp)
    print("Accessing dynamic attribute s1.num_spells:", s1.num_spells)
    print()

    print("\n========== END OF DEMO ==========\n")
