from dataclasses import dataclass,field
from typing import List
from sympy import Symbol,Expr

@dataclass
class PartialDerivative:
    variable:str =""
    expression:str =""

@dataclass
class PartialDerivatives:
    values:List[PartialDerivative]= field(default_factory=list)


@dataclass
class Derivative:
    name:str = ""
    expression:str =""
    variables:List[str] = field(default_factory=list)
    partial_derivatives: PartialDerivatives = field(default_factory=lambda: PartialDerivatives(values=[]))
    evaluated_point: List[float] = field(default_factory=list)

@dataclass
class Derivatives:
    parents:List[Derivative] = field(default_factory=list)
    childs:List[Derivative] = field(default_factory=list)

@dataclass
class DerivativeValue:
    type:str =""
    value:str=""

@dataclass
class Expression:
    type:str =""
    value:str =""
    name:str = ""


@dataclass
class Expressions:
    values:List[Expression] = field(default_factory=list)

@dataclass
class Variables:
    value:List[str] = field(default_factory=list)
