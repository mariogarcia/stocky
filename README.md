## Event Sourcing Example

This repository is a proof of concept for creating a very simple REST API using event-sourcing in Python. It uses 

- [eventsourcing](https://github.com/johnbywater/eventsourcing) library to implement the event sourcing core.
- [Fast API](https://fastapi.tiangolo.com/) for exposing a REST API

## Configuration

The application uses SQLITE as persistence engine. Notice that depending on the execution environment, **.env** variables (VisualStudio) or **setup_event_sourcing()** will be used.

## Idea

The idea is to at least implement the following concepts:

- Events
- Aggregates
- Producers
- Basic Command-Query segregation

### Events

**Every information is stored as an event**. An event is always related to an aggregate, and eventually a stream of events will represent the state of an aggregate at a given point in time.

**Clients don't consume information directly from events**, but from materialized views built from events or aggregates.

### Aggregate

An aggregate represents **the state of a concept in the system** at a given point in time.

### Producers

Producers are aware of events an aggregates and usually **are used to build efficient views to be consumed by clients**. These views are built to be performant and could be destroyed at any time and built again from the event stream.

Clients don't consume events, or aggregates directly but specialized views built by producers.

### Command - Query segregation

**In a system where reads are more frequent than writes** a command/query architecture may bring you some benefits like for example, having more efficient and scalable reads.

#### Efficient reads

In a system where reads are more frequent than writes is very helpful to be capable to build specialized read-only views, that can be replicated without the bottleneck of being accessed for writing.

Thus writes will be done to a single node. Several producers will build specialized (and maybe cached) views that can be scaled vertically or horizontally without worrying about writing bottlenecks.

Of course that doesn't come free, the cost is **eventual consistency**. The writes takes some time to be propagated, and that is something that has to be considered when designing the rest of the system, specially when updating client's views.

#### Isolation

**Designing a system in a Command/Query from the beginning doesn't mean you have to go microservices right away**. 

You can start by designing your Python's modules with a clear separation and isolation. In other words everything inside the command modules can't have any dependency with the query modules and viceversa. Later on that will enable you to convert those models in different deployable applications.

Of course there could be some modules that can be considered common to both command/query, like utility classes, or boilerplate code that is always used in both modules. As a rule of thumb, remember that **everything that can be considered part of the business logic, that must remain confined, and never shared**.

## Conclusions

TODO