# ADR-0001 Runtime Architecture

## Status

Accepted

## Context

ECHO requires a lightweight runtime to manage system lifecycle.

## Decision

The runtime is responsible for:

- Module registration
- Module initialization
- Module startup
- Module shutdown

The runtime is NOT responsible for:

- Memory
- LLM
- Chat
- GUI

## Consequences

Future capabilities must be implemented as EchoModule.