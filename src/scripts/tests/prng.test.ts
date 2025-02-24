import { describe, expect, test } from 'vitest';
import { prng } from '../prng';

describe('PRNG consistency', () => {
    test('Seed returns same result', () => {
        const seed = Math.random() * 1e6;
        expect(prng(seed)).to.eq(prng(seed));
    });

    test('Seed return same result across tests', () => {
        const seed = 73.245;
        expect(prng(seed)).toMatchInlineSnapshot(`0.793203140841797`);
    });
});
