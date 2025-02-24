import Rand from 'rand-seed';

export function prng(seed: number): number {
    const stringSeed: string = btoa(seed.toString());
    return new Rand(stringSeed).next();
}
