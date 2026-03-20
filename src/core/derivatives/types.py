from dataclasses import dataclass,field
from typing import List
from sympy import Symbol,Expr


@dataclass
class IVectorGradient:
    values:List[float] = field(default_factory=list)


@dataclass
class IDerivative:
    name:str = ""
    expression:str = ""
    variables:List[str] = field(default_factory=list)
    evaluated_point: List[float] = field(default_factory=list)

@dataclass
class IPartialDerivative:
    variable:str =""
    expression:str =""

@dataclass
class IPartialDerivatives:
    values:List[IPartialDerivative]= field(default_factory=list)
    variables:List[str] = field(default_factory=list)


@dataclass
class IDerivatives:
    first_partials:IPartialDerivatives = field(default_factory=lambda: IPartialDerivatives(values=[]))
    second_partials:IPartialDerivatives = field(default_factory=lambda: IPartialDerivatives(values=[]))


@dataclass
class IFunction:
    name:str = ""
    expression:str = ""
    variables:List[str] = field(default_factory=list)
    derivatives:IDerivatives = field(default_factory=lambda: IDerivatives(values=[]))
    evaluated_point: List[float] = field(default_factory=list)

@dataclass
class IHierarchyFunctions:
    parents:List[IFunction] = field(default_factory=list)
    childs:List[IFunction] = field(default_factory=list)


@dataclass
class Expression:
    type:str =""
    value:str =""
    name:str = ""


@dataclass
class Expressions:
    values:List[Expression] = field(default_factory=list)
