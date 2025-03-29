# SOLID principles implementation
This is a repo used to practice and visualize the SOLID principles in software development.

The main reference for this repo will be [Martin, R. C. (2018). Clean Architecture:
A Craftsman's Guide to Software Structure and Design Pearson Education Inc](amzn.to/442LA9R)

## Dependency Inversion Principle (DIP)

### Description

This principle is implemented in package (Dip).

This code demonstrates how dependencies can be inverted using interfaces (abstract classes).

The idea is that the concrete/instable/low level implementations should be imported
the least possible, making the higher level code with the business logic less dependent on them
and thus more stable.

The inversion in dependency expression comes from the fact that normally the
dependency flow is the same of control flow (higher level modules call and import
lower level modules), but this introduces instability to the higher level code.
Thus, one should aim for relying mainly on interfaces imports.

I simulated a few computing operations that are abstractly created in the interfaces module.
I also created an abstract factory to facilitate implementation of the computers.

The abstract classes are then implemented using concrete classes in the concrete
module. Thus, there is a control. The main module, entrypoint, needs to import
only the concrete implementation of the factory (this break of the DIP principle
in practice is expected and sometimes unavoidable).

### Running the module

```bash
python3 -m Dip.main --a first_number --b second_number --computer_type computer_type
```
**where**: `computer_type` should be either `sum` or `product`
